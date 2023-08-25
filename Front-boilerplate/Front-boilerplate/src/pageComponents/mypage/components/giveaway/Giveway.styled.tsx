import styled from "styled-components"

const Giveway = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`

const GiveBodyLayout = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid rebeccapurple;
    width: 100%;
`

const GiveTitle = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid indigo; */
    padding : 20px 0px 20px 40px;
    font-size: 38px;
`

const GiveBody = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid ${(props) => props.theme.colors.ssafy};
    width: 1000px;
    height: auto;
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    background-color: ${(props) => props.theme.colors.middle};
`

const GiveCard = styled.div.attrs<any>((props) => ({}))`
    padding: 30px;
`

const GiveGoodsLayout = styled.div.attrs<any>((props) => ({}))`
    padding: 30px 0px 30px 0px;
`

const GiveGoodsTitle = styled.div.attrs<any>((props) => ({}))`
    margin: 10px;
    font-size: 21px;
`

export{
    Giveway, GiveBodyLayout, GiveBody, GiveTitle, GiveCard, GiveGoodsLayout, GiveGoodsTitle
}