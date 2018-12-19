import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render () {
        return <div>{'test-view'}</div>;
    }
}

import '../../../scss/index.scss';

ReactDOM.render(
    <App/>,
    document.getElementById('test-view')
);
