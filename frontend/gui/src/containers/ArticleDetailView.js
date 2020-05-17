import React, { Component } from 'react';
import Article from '../components/Article';
import axios from 'axios';

class ArticleDetail extends Component {
    state = {
        articles: []
    }

    componentDidMount() {
        const articleid = this.props.match.params.articleid
        axios.get(`http://127.0.0.1:8000/api/auth/customer/${articleid}`).then(
            res => {this.setState({articles: [res.data]});
            console.log(this.state.articles)}
        )
        
    }
    render() {
        return (
            <Article data={this.state.articles}/>
        )
    }
}

export default ArticleDetail;

