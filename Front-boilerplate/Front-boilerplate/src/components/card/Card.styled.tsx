import styled, {css} from "styled-components"

const StyledCard = styled.div.attrs<any>((props) => ({}))`
    ${(props) => {
        const use = props.use || "basic";

        const UseStyled : any = {
            basic : `
                border : solid 1.3px black;
            `,
            giveway : `
                border : solid 1.3px black;
            `
        }

        return css`  
            display: flex;
            flex-direction: column;
            width: 150px;
            height: 180px;
            margin: 10px;
            ${UseStyled[use]}
        `
    }}
   
`

const CardBody = styled.div.attrs<any>((props) => ({}))`
    width: 100%;
    height: 140px;
    display: flex;
    justify-content: center;
    align-items: center;
`

const CardImg = styled.img.attrs<any>((props) => ({}))`
    width: 100%;
    height: 100%;
`

const CardTitle = styled.div.attrs<any>((props) => ({}))`

${(props) => {
        const use = props.use || "basic";

        const UseStyled : any = {
            basic : `
                border-top : solid 1.3px black;
            `,
            giveway : `
                background-color : #ffffff;
                border-top : solid 1.3px black;
            `
        }

        return css`
            width: 100%;
            height: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            ${UseStyled[use]}
        `
    }}
`

export {
    StyledCard, CardTitle, CardBody, CardImg
}