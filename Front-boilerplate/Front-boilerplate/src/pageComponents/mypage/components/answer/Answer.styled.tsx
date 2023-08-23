import { styled } from "styled-components"

const Answer = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`

const AnswerProfile = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid blue; */
    width: 100%;
    height: 200px;
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

const AnswerBody = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid ${(props) => props.theme.colors.ssafy};
    width: 750px;
    height: 400px;
    margin-top: 20px;
    display: flex;
    flex-direction: column;
`

const AnswerBodySlectBox = styled.div.attrs<any>((props) => ({}))`
    display: flex;

`

const AnswerBodySlect = styled.div.attrs<any>((props) => ({}))`
    background-color: ${(props) => props.stateName === props.name ? props.theme.colors.middle : "#ffffff"};
    width: 100px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
`

const AnswerBodyInfo = styled.div.attrs<any>((props) => ({}))`
    background-color: ${(props) => props.theme.colors.middle};
    width: 100%;
    height: 395px;
`

export {
    Answer, AnswerProfile, AnswerProfileImg, AnswerProfileBody, AnswerProfileText, AnswerProfileTextBox, AnswerBody, AnswerBodySlect, AnswerBodyInfo, AnswerBodySlectBox
}