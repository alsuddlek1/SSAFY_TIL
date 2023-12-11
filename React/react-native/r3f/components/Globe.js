import React from "react";
import { useRef } from "react";
import { Canvas, useFrame } from '@react-three/fiber'
// import { OrbitControls } from "@react-three/drei/native";

const CustomGlobe = () => {
    const refMesh = useRef()

    // 회전 
    // useFrame((state, delta) => {
    //     refMesh.current.rotation.y += delta
    // })
    // <directionalLight position={[1, 1, 1]} rotation-y={45*Math.PI/180}/>

    return(
        <>
        <directionalLight position={[1, 1, 1]} />

        <axesHelper scale={10} /> 
        {/* <OrbitControls /> */}

        <mesh ref={refMesh} >
            <boxGeometry />
            <meshStandardMaterial color="#e67e22" />
        </mesh>
        </>
    )
}

export default CustomGlobe;