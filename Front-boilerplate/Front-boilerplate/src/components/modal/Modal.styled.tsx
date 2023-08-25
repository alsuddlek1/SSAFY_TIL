import styled from 'styled-components'

const Modal = styled.div.attrs<any>((props) => ({}))`
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
    position: fixed;
    top: 0;
    left: 0;
`

const ModalWindow = styled.div.attrs<any>((props) => ({}))`
    width: 150px;
    height: 100px;
    border: 1px solid aquamarine;
    background-color: #fff;
    position: fixed;
    top: 50%;
    left: 50% ;
`

export {
    Modal, ModalWindow
}