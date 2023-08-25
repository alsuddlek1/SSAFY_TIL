import React from "react";
import { StyledCard, CardTitle, CardBody, CardImg } from "./Card.styled"
import Image from "next/image";


const CardComponent = (props:any) => {
    return (
        <StyledCard {...props}>
            <CardBody>
                <CardImg src={props.img} />
            </CardBody>
            <CardTitle {...props}>
                {props.title}
            </CardTitle>
        </StyledCard>
    )
};

export default CardComponent