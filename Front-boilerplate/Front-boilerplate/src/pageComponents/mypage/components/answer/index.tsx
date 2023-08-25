'use client'

import {Answer, AnswerBody, AnswerBodySlect, AnswerBodyInfo, AnswerBodySlectBox, AnswerBodyLayout } from "./Answer.styled"
import Answered from "../answered"
import Made from "../made"
import {useState} from 'react'
import Profile from '../profile'


const answer = () => {
    const [state, setState] = useState("answered")

    return(
        <Answer>
            <Profile/>
        <AnswerBodyLayout>
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
        </AnswerBodyLayout>
        </Answer>
    )
}

export default answer