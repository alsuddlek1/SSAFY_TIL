'use client'

import {Answer, AnswerProfile, AnswerProfileImg, AnswerProfileBody, AnswerProfileText, AnswerProfileTextBox, AnswerBody, AnswerBodySlect, AnswerBodyInfo, AnswerBodySlectBox } from "./Answer.styled"
import Image from "next/image"
import Answered from "../answered"
import Made from "../made"
import {useState} from 'react'


const answer = () => {
    const [state, setState] = useState("answered")

    return(
        <Answer>
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
        <div>

        <AnswerBody>
            <AnswerBodySlectBox>
                <AnswerBodySlect stateName={state} name="answered" onClick={() => setState("answered")}>
                    응답한설문
                </AnswerBodySlect>
                <AnswerBodySlect stateName={state} name="made" onClick={() => setState("made")}>
                    만든 설문
                </AnswerBodySlect>
            </AnswerBodySlectBox>
            <AnswerBodyInfo>
                {state === "answered" && <Answered/>}
                {state === "made" && <Made/>}
            </AnswerBodyInfo>
        </AnswerBody>
        </div>
        </Answer>
    )
}

export default answer