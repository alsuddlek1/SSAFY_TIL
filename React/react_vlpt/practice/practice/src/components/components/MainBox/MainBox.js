import React from "react";
import MainBox from "./MainBox.css"
import Home from "../Home/Home"

// 핸드폰 메인 프레임 (+ 상단바)
function mainBox() {
    return(
        <div className="mainbox">
            갤럭시
            <div className="topbar">
                상단바
            </div>
            <div>
                <Home/>
            </div>
        </div>
    )
}

export default mainBox