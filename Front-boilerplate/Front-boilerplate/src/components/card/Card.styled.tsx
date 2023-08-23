import styled, {css} from "styled-components"

const StyledCard = styled.div.attrs<any>((props) => ({}))`
    ${(props) => {
        return css`
             border : 1px solid black;
            border-radius: 10%;
            width: 100px;
            height: 100px;
        `
    }}
   
`

export {
    StyledCard
}