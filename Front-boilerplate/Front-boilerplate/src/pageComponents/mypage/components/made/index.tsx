'use client'

import { MadeLayout, MadeLine1, MadeLine2 } from "./Made.styled"
import Card from "@/components/card"

const Made = () => {
    return (
        <MadeLayout>
            <MadeLine1>
                <Card title="1번 설문" img="/cow.jpg"></Card>
                <Card title="2번 설문"></Card>
                <Card title="3번 설문"></Card>
                <Card title="4번 설문"></Card>
            </MadeLine1>
            <MadeLine2>
                <Card title="5번 설문" img="/cow.jpg"></Card>
                <Card title="6번 설문"></Card>
                <Card title="7번 설문"></Card>
            </MadeLine2>
        </MadeLayout>
    )
}

export default Made;