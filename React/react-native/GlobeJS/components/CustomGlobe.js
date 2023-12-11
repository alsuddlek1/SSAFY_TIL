import React, { useRef } from "react";
import { useFrame } from "@react-three/fiber";
import useControls from "r3f-native-orbitcontrols"
import { Canvas } from "@react-three/fiber";
import { View } from "react-native";


const CustomGlobe = () => {
    const refMesh = useRef()
    return(
        <Canvas>
        <>
            <directionalLight position={[1, 1, 1]} />

            <axesHelper scale={10} /> 

            <mesh ref={refMesh} >
                <boxGeometry />
                <meshStandardMaterial color="#e67e22" />
            </mesh>
        </>
        </Canvas>
    )
}

export default CustomGlobe;