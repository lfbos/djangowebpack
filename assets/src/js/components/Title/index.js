import React from 'react';
import styled from 'styled-components'

const Button = styled.a`
    display: inline-block;
    border-radius: 3px;
    padding: 0.5rem 0;
    margin: 0.5rem 1rem;
    width: 11rem;
    background: transparent;
    color: blue;
    border: 2px solid blue;
    text-align: center;
`;

const Header = styled.a`
    font-size: 3rem;
    display: block;
`;

const Title = ({text}) => {
    return (
        <div>
            <Button>Hi!</Button>
            <Header className="title">{text}</Header>
        </div>
    )
};

export default Title;
