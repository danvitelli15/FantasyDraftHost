const element = React.createElement

class PlayerPanel extends React.Component {
    render() {
        return ('div', null, element(PlayerBasics, null), element(PlayerDetails, null));
    }
}

class PlayerBasics extends React.Component {
    render() {
        return ('div', null, 'player basic information');
    }
}

class PlayerDetails extends React.Component {
    render() {
        return ('div', null, 'player stats information');
    }
}

ReactDOM.render(
    element(PlayerPanel),
    document.querySelector('#PlayerPanel')
);