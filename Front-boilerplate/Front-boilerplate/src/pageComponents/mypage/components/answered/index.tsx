'use client'

import { AnsweredLayout, AnsweredLine1, AnsweredLine2 } from "./Answered.styled";
import Card from "@/components/card"


const Answered = () => {
    return(
        <AnsweredLayout>
            <AnsweredLine1>
                <Card/>
            </AnsweredLine1>
            <AnsweredLine1>
                <Card/>
            </AnsweredLine1>
        </AnsweredLayout>
    )
}

export default Answered;