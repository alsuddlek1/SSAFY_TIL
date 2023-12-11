import React from "react"

function Hello({color, name, isSpeacial}) {
    return(

        <div style={{color:color}}>
            {isSpeacial ?<b>*</b> : null}
            {/* isSpeacial 값이 ture 라면 * 아니라면 null  아래도 같은 표현 */}
            {isSpeacial && <b>*</b>}
            안녕하세용!!
            {name}
        </div>
            )
}

Hello.defaultProps = {
    name:'이름없음'
}

export default Hello