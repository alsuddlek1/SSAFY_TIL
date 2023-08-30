'use client'

import Image from "next/image";
import { Modal, ModalWindow, ModalBody, ModalImg, ModalContent, ModalButton } from "./Modal.styled";
import Button from "@/components/button"

const modal = (props:any) => {
    return (
        <Modal onClick={props.closeModal} >
            <ModalWindow>
                <ModalBody>
                    <ModalImg>
                        <Image src="/cow.jpg" width={100} height={100} alt="modalImg" />
                    </ModalImg>
                    <ModalContent>
                        
                        <ModalButton>
                            <Button label="저장" use="save"></Button>
                            <Button label="공유" use="share"></Button>
                        </ModalButton>
                    </ModalContent>
                </ModalBody>
            </ModalWindow>
        </Modal>
    )
}

export default modal;