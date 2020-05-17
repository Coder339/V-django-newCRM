import React from 'react';
import ArticleList from './containers/ArticleListView';
import ArticleDetail from './containers/ArticleDetailView';
import { Route } from 'react-router-dom';

const BaseRoute = () => (
    <div>
        <Route exact path='/' component={ArticleList}/>
        <Route exact path='/:articleid' component={ArticleDetail}/>
    </div>
        
    
)

export default BaseRoute;