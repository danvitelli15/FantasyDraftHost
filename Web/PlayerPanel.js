class PlayerPanel extends React.Component {
    render() {
        return ('div', null, element(PlayerBasics, {Name: "Daniel Vitelli"}));
    }
}

class PlayerBasics extends React.Component {
    render() {
        return ('div', null, h2(this.props.Name));
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