'use client'

import { Modal, ModalWindow } from "./Modal.styled";

const modal = (props:any) => {
    return (
        <Modal onClick={props.closeModal} >
            <ModalWindow>
                헤헤
            </ModalWindow>
        </Modal>
    )
}

export default modal;