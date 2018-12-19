import json
import os
import subprocess
import time

from django.conf import settings
from django.template.loader import render_to_string
from termcolor import cprint
from tqdm import tqdm


class NewViewBuilder:
    templates_dir = os.path.join(settings.TEMPLATES[0].get('DIRS')[0], 'frontend')
    js_assets_dir = os.path.join(settings.BASE_DIR, 'assets', 'src', 'js', 'apps')
    base_html_template = 'frontend/base.html'
    base_js_template = 'frontend/base.js'
    entry_point = None

    def __init__(self, view_name, title):
        self.view_name = view_name
        self.title = title
        self.template_path = os.path.join(self.templates_dir, '{}/index.html'.format(view_name))
        self.view_app = view_name.replace('_', '-')

        self.context = {
            'title': title,
            'view_app': self.view_app,
            'load_libraries': '{% load render_bundle from webpack_loader %}',
            'bundle_css': "{% render_bundle '" + view_name + "' 'css' %}",
            'bundle_js': "{% render_bundle '" + view_name + "' 'js' %}"
        }
        self.pbar = tqdm(total=100)

    def run(self):
        self._create_entry_point()
        self._create_js_files()
        self._create_template()
        self.pbar.close()

        cprint(
            "View created successfully! You should now associate this template to a view or url in django.",
            'green',
            attrs=['bold']
        )

    def _create_entry_point(self):
        entry_points_file = os.path.join(settings.BASE_DIR, 'entry_points.json')

        with open(entry_points_file) as f:
            self.pbar.update(10)
            entry_points = json.load(f)
            time.sleep(0.1)

            if self.view_name in entry_points.keys():
                raise Exception('There is already an app with that name')

            self.entry_point = os.path.join('assets', 'src', 'js', 'apps', self.view_name, 'index.js')

            self.pbar.update(10)
            entry_points[self.view_name] = self.entry_point

            time.sleep(0.1)

        with open(entry_points_file, 'w') as f:
            self.pbar.update(10)
            json.dump(entry_points, f)
            time.sleep(0.1)

        self.pbar.update(10)
        time.sleep(0.1)

    def _create_js_files(self):
        content = render_to_string(self.base_js_template, {'view_app': self.view_app})
        view_app_dir = os.path.join(self.js_assets_dir, self.view_name)
        index_js_file = os.path.join(view_app_dir, 'index.js')

        self.pbar.update(10)
        os.mkdir(view_app_dir)
        time.sleep(0.1)

        self.pbar.update(10)
        with open(index_js_file, 'w') as js_file:
            js_file.write(content)

        self.pbar.update(5)
        time.sleep(0.1)

        subprocess.call(['npm', 'run', 'build'], stdout=subprocess.PIPE)

        self.pbar.update(5)
        time.sleep(0.1)

    def _create_template(self):
        content = render_to_string(self.base_html_template, self.context)

        self.pbar.update(10)
        view_template_dir = os.path.join(self.templates_dir, self.view_name)
        os.mkdir(view_template_dir)
        time.sleep(0.1)

        self.pbar.update(10)
        with open(self.template_path, 'w') as static_file:
            content = content.replace("&#39;", "'")
            static_file.write(content)
        time.sleep(0.1)

