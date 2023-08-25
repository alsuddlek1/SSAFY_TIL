import styled from "styled-components"

const AnsweredLayout = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    flex-direction: column;
    padding: 20px;
`

const AnsweredLine1 = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    justify-content: space-between;
`

const AnsweredLine2 = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    justify-content: space-between;
`

export {
    AnsweredLayout, AnsweredLine1, AnsweredLine2
}