'use client'

//index : 보여질(?) 페이지 (styled에서 가져옴)

import {Mypage, MypageNav, MypageNavSelect, MypageLayout} from './Mypage.styled'
import Myinfo from './components/myinfo'
import Answer from './components/answer'
import { useState } from 'react'


const myPage = () => {
    const [state, setState] = useState("myinfo")
    
    return(
        <Mypage>
        <MypageNav>
            <MypageNavSelect onClick={() => setState("myinfo")}>
                회원정보
            </MypageNavSelect>
            <MypageNavSelect onClick={() => setState("answer")}>
                설문 현황
            </MypageNavSelect>
            <MypageNavSelect>
                만든 설문
            </MypageNavSelect>
            <MypageNavSelect>
                당첨 상품
            </MypageNavSelect>
        </MypageNav>
            <MypageLayout>

            {state === 'myinfo' && <Myinfo/>}
            {state === 'answer' && <Answer/>}
            </MypageLayout>
            
        </Mypage>
    )
}

export default myPage