'use client'

import { AnswerProfile, AnswerProfileImg, AnswerProfileBody, AnswerProfileText, AnswerProfileTextBox } from "./Profile.styled"
import Image from "next/image"


const profile = () => {
    return (        
        <AnswerProfile>
            <AnswerProfileImg>
                <Image src="/cow.jpg" width={100} height={100} alt="answerImg"></Image>
            </AnswerProfileImg>
            <AnswerProfileBody>
                <AnswerProfileTextBox>
                    <AnswerProfileText>
                        김설문조사
                    </AnswerProfileText>
                    <AnswerProfileText>
                        김설문/1999-02-10/남자
                    </AnswerProfileText>
                </AnswerProfileTextBox>
                <AnswerProfileTextBox>
                    <AnswerProfileText>
                        응답한 설문 : 100
                    </AnswerProfileText>
                    <AnswerProfileText>
                        만든 설문 : 5
                    </AnswerProfileText>
                    <AnswerProfileText>
                        당첨된 상품 : 10
                    </AnswerProfileText>
                </AnswerProfileTextBox>
            </AnswerProfileBody>
        </AnswerProfile>
    )
}

export default profile