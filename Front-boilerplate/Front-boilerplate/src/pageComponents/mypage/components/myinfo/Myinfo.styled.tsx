import styled from 'styled-components'

const Myinfo = styled.div.attrs<any>((props) => ({}))`
    border: 1px solid antiquewhite;
    margin-left: 150px;
    margin-right: 150px;
`

const MypageTitle = styled.div.attrs<any>((props) => ({}))`
    /* border : 1px solid red; */
    padding-top: 30px;
    padding-left: 20px;
`

const MypageProfileImg = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid orange; */
    display: flex;
    justify-content: center;
    padding-top: 30px;
`

const MypageBody = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid blue; */
    padding-left: 20px;
    line-height: 35px;
`

const MypageInfo = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid yellowgreen; */
    padding: 10px;
`

const MypageInput = styled.div.attrs<any>((props) => ({}))`
    display: flex;
`

const MypageButton = styled.div.attrs<any>((props) => ({}))`
    /* border: 1px solid rebeccapurple; */
    padding-bottom: 10px;
    padding-top: 10px;
    padding-left: 20px;
`

export {
    MypageTitle, MypageProfileImg, MypageBody,MypageInfo, MypageInput, MypageButton, Myinfo
}