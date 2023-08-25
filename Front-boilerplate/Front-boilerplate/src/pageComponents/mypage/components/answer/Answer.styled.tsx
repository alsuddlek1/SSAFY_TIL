import styled from "styled-components"

const Answer = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`



const AnswerBodyLayout = styled.div.attrs<any>((props) => ({}))`
    width: 100%;
`

const AnswerBody = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid ${(props) => props.theme.colors.ssafy};
    width: 1000px;
    height: auto;
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
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
    height: auto;
`

export {
    Answer, AnswerBody, AnswerBodySlect, AnswerBodyInfo, AnswerBodySlectBox, AnswerBodyLayout
}