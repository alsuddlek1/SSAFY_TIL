import React from "react";
import { StyledCard } from "./Card.styled"


const CardComponent = (props:any) => {
    return (
        <StyledCard>{props.title}</StyledCard>
    )
};

export default CardComponent