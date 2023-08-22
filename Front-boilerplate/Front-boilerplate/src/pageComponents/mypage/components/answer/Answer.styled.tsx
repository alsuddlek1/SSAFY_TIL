import { styled } from "styled-components"

const AnswerProfile = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid blue;
    width: 100%;
    height: 230px;
    display: flex;
    padding: 30px;
`

const AnswerProfileImg = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid red;
    height: 120px;
    width: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
`

const AnswerProfileBody = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid aqua;
    display: flex;
`

const AnswerProfileTextBox = styled.div.attrs<any>((props) => ({}))`
    border : 1px solid black;
`

const AnswerProfileText = styled.div.attrs<any>((props) => ({}))`
    border : 1px solid blueviolet
`

export {
    AnswerProfile, AnswerProfileImg, AnswerProfileBody, AnswerProfileText, AnswerProfileTextBox
}