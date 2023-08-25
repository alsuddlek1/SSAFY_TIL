'use client'

//index : 보여질(?) 페이지 (styled에서 가져옴)

import {Mypage, MypageNav, MypageNavSelect, MypageLayout} from './Mypage.styled'
import Myinfo from './components/myinfo'
import Answer from './components/answer'
import Giveway from './components/giveaway'
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
            <MypageNavSelect onClick={() => setState("giveway")}>
                당첨 상품
            </MypageNavSelect>
            <MypageNavSelect>
                포인트 사용
            </MypageNavSelect>
        </MypageNav>
            <MypageLayout>

            {state === 'myinfo' && <Myinfo/>}
            {state === 'answer' && <Answer/>}
            {state === 'giveway' && <Giveway/>}
            </MypageLayout>
            
        </Mypage>
    )
}

export default myPage