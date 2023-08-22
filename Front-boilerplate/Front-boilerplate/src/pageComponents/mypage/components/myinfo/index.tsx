'use client'

import {Myinfo, MypageTitle, MypageProfileImg, MypageBody, MypageInfo , MypageInput, MypageButton} from "./Myinfo.styled"
import Input from '@/components/input'
import Button from '@/components/button'
import Image from "next/image"

const myinfo = () => {
    return(
        <Myinfo>
            <MypageTitle>
            <h2>내정보수정</h2>
            <hr/>
            </MypageTitle>
            <MypageProfileImg>
            <Image src="/cow.jpg" width={100} height={100} alt='profileImg'></Image>
            </MypageProfileImg>
            <MypageBody>
                <MypageInfo>
                    <h3>이메일</h3>
                    <MypageInput>
                        <Input use='mypage' placeholder='이메일을 입력하세요'></Input>
                    </MypageInput>
                </MypageInfo>
                <MypageInfo>
                    <h3>생일</h3>
                    <MypageInput>
                        <Input placeholder='년도' type='number' use='mypage'></Input>
                        <Input placeholder='월' type='number' use='mypage'></Input>
                        <Input placeholder='일' type='number' use='mypage'></Input>
                    </MypageInput>
                </MypageInfo>
                <MypageInfo>
                    <h3>닉네임</h3>
                    <MypageInput>
                        <Input placeholder='닉네임을 입력하세요' use='mypage'></Input>
                    </MypageInput>
                </MypageInfo>
                <MypageInfo>
                    <h3>성별</h3>
                    <MypageInput>
                        <Input placeholder='성별을 입력하세요' use='mypage'></Input>
                    </MypageInput>
                </MypageInfo>
                <MypageButton>
                    <Button label='수정'></Button>
                    <Button label='탈퇴' use='error'></Button>
                </MypageButton>
            </MypageBody>
        </Myinfo>
    )
}

export default myinfo