import React, { Component } from 'react';
import './style.css';
import {Icon} from 'antd'

class Header extends Component{
    state = {
        isLoggedIn : this.props.isLoggedIn
    }

    toggleLoggedIn = () => {
        this.setState(prev => ({isLoggedIn: !prev.isLoggedIn}))
    }
    render(){
        const {title} = this.props;
        const {isLoggedIn} = this.state;
        return (
            <div className="header">
                <Icon type="ant-design" />
                <div className="name"><h1>Stack<span className="name1">overflowClone</span></h1></div>
                <div className="menu" onClick={this.toggleLoggedIn}>
                {
                    isLoggedIn ? <h1><span className="name1">Logout</span></h1> : <h1><span className="name1">Login</span></h1>
                }
                </div>
            </div>
        )
    }
}

export default Header