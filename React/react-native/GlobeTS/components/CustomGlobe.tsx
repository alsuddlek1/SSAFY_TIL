import React, { useRef } from "react";
import { useFrame } from "@react-three/fiber";


const CustomGlobe = () => {
    const refMesh = useRef<any>()
    useFrame((state, delta) => {
        refMesh.current.rotation.y += delta
    })
    return(
        <>
        
            <mesh ref={refMesh} rotation-y={45*Math.PI/180}>
                <boxGeometry />
                <meshStandardMaterial color="#d8536a" />
            </mesh>
        </>
    )
}

export default CustomGlobe;