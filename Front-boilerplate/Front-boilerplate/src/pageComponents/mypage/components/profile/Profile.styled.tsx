import styled from "styled-components"

const AnswerProfile = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid blue; */
    width: 100%;
    height: 170px;
    display: flex;
    padding: 30px;
    background-color: ${(props) => props.theme.colors.base};
    
`

const AnswerProfileImg = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid red; */
    height: 120px;
    width: 120px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 50px;
`

const AnswerProfileBody = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid aqua; */
    width: 600px;
    display: flex;
    justify-content: space-around;
`

const AnswerProfileTextBox = styled.div.attrs<any>((props) => ({}))`
    /* border : 1px solid black; */
    display: flex;
    flex-direction: column;
    padding-top: 10px;
`

const AnswerProfileText = styled.div.attrs<any>((props) => ({}))`
    /* border : 1px solid blueviolet; */
    padding: 5px;
`

export {
    AnswerProfile, AnswerProfileImg, AnswerProfileBody, AnswerProfileText, AnswerProfileTextBox
}