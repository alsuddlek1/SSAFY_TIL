'use client'

import { SignUpPage, ButtonDiv, SignupBirth} from "./Signup.styled"
import Input from '@/components/input'
import Button from '@/components/button'
import { useEffect, useState } from "react"
import useUserStore from "@/stores/useUserStore"


const signUp = () => {
    const userInfo = useUserStore((state:any) => state.user)
    const setUseUser = useUserStore((state:any) => state.setUseUser)
    const [user, setUser] = useState({
        name : "",
        email: "",
        year : "",
        month : "",
        day : "",
        password : "",
        passwordCheck : ""
    })

    const onChange = (e:any) => {
        const name = e.target.name
        const value = e.target.value

        setUser({
            ...user,
            [name] : value
        })
    }


    const submit = () => {
        setUseUser(user)
    }
    return(
        <SignUpPage>
            <h2>회원가입</h2>
            <br />
            <Input name="name" placeholder="이름" onChange={onChange}></Input>
            <Input name="email" placeholder="이메일" onChange={onChange}></Input>
            <SignupBirth>
                <Input name="year" placeholder="연도" type="number" use="signup" onChange={onChange}></Input>
                <Input name="month" placeholder="월" type="number" use="signup" onChange={onChange}></Input>
                <Input name="day" placeholder="일" type="number" use="signup" onChange={onChange}></Input>
            </SignupBirth>
            <Input name="password" placeholder="비밀번호" onChange={onChange} type="password"></Input>
            <Input name="passwordCheck" placeholder="비밀번호 확인" onChange={onChange} type="password"></Input>
            <br/>
            <ButtonDiv>
            <Button label="SignUp" type="submit" onClick={submit}></Button>
            </ButtonDiv>
        </SignUpPage>
    )
}

export default signUp