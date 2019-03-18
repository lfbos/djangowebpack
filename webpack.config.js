const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractText = require('extract-text-webpack-plugin');
const WebpackBuildNotifierPlugin = require('webpack-build-notifier');

const entries = require('./entry_points.json');

const entryPoints = () => {
    const entryPointObject = {};
    for (let key in entries) {
        entryPointObject[key] = path.join(__dirname, entries[key])
    }

    return entryPointObject;
};

module.exports = {
    entry: entryPoints(),
    output: {
        path: path.join(__dirname, 'assets/dist'),
        filename: '[name]-[hash].js'
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: 'webpack-stats.json'
        }),
        new ExtractText({
            filename: '[name]-[hash].css'
        }),
        new WebpackBuildNotifierPlugin({
            title: "Proyect Example Build",
            // logo: path.resolve('/path/to/project/logo'),
            successSound: true,
            compilationSound: true,
            failureSound: true
        })
    ],
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                loader: ['style-loader', 'css-loader']
            }, {
                test: /\.scss$/,
                use: ExtractText.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'sass-loader']
                })
            }
        ]
    }
};