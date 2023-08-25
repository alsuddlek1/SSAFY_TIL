import styled from "styled-components"

const MadeLayout = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    flex-direction: column;
    padding: 20px;
`

const MadeLine1 = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    justify-content: space-between;
`

const MadeLine2 = styled.div.attrs<any>((props) => ({}))`
    display: flex;
    justify-content: space-between;
`

export {
    MadeLayout, MadeLine1, MadeLine2
}