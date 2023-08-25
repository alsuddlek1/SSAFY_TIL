'use client'

import { useEffect, useState } from "react";
import Profile from "../profile"
import { Giveway, GiveBodyLayout, GiveBody, GiveTitle, GiveCard, GiveGoodsLayout, GiveGoodsTitle } from "./Giveway.styled";
import Card from "@/components/card"
import Modal from "@/components/modal"

const giveway = () => {

    const [isOpen, setIsOpen] = useState(false)

    useEffect(() => {
        console.log(isOpen)
    }, [isOpen])
    
    const closeModal = () => {
        setIsOpen(false)
    }
    return(
        <Giveway>
            <Profile/>
            <GiveBodyLayout>
                <GiveTitle>
                    당첨된 선물
                </GiveTitle>
                <GiveBody>
                    <GiveCard>
                        <Card title="1번 설문" img="/cow.jpg" use="giveway" onClick={() => setIsOpen(true)}/>
                    </GiveCard>
                    <GiveGoodsLayout>
                        <GiveGoodsTitle>
                            치킨
                        </GiveGoodsTitle>
                    </GiveGoodsLayout>
                </GiveBody>
            </GiveBodyLayout>
            { isOpen === true &&  <Modal isOpen={isOpen} closeModal={closeModal} />}
        </Giveway>
    )
}

export default giveway;