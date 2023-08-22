import styled from 'styled-components'

const SignUpPage = styled.div.attrs<any>((props) => ({}))`
    margin: 100px auto;
    width: 420px;
    padding: 50px;
    border: 2px solid #e7e7e7;
    border-radius: 5px;
`

const ButtonDiv = styled.div.attrs<any>((props) => ({}))`
    margin-top: 10px;
`

export {
    SignUpPage, ButtonDiv
}