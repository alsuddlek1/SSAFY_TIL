import { styled } from "styled-components"

const Mypage = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid yellow; */
    display: flex;
    height: 640px;
    /* justify-content: center; */
`

const MypageLayout = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid red;
    width: 100%;
`


const MypageNav = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid black;
    padding: 10px;
    width: 300px;
`

const MypageNavSelect = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid rebeccapurple; */
    padding: 3px;
    margin: 5px;
    font-size: 20px;
`


export {
    Mypage,  MypageNav, MypageNavSelect, MypageLayout
}