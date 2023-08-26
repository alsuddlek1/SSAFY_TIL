'use client'

import { Modal, ModalWindow } from "./Modal.styled";

const modal = (props:any) => {
    return (
        <Modal onClick={props.closeModal} >
            <ModalWindow>
                상품정보
            </ModalWindow>
        </Modal>
    )
}

export default modal;