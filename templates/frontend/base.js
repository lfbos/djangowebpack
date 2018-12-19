import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render () {
        return <div>{'{{view_app}}'}</div>;
    }
}

import '../../../scss/index.scss';

ReactDOM.render(
    <App/>,
    document.getElementById('{{ view_app }}')
);
