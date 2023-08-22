'use client'

import { SignUpPage, ButtonDiv} from "./Signup.styled"
import Input from '@/components/input'
import Button from '@/components/button'


const signUp = () => {
    return(
        <SignUpPage>
            <h2>회원가입</h2>
            <br />
            <Input placeholder="이메일"></Input>
            <Input placeholder="비밀번호"></Input>
            <br/>
            <ButtonDiv>
            <Button label="SignUp" type="submit"></Button>
            </ButtonDiv>
        </SignUpPage>
    )
}

export default signUp