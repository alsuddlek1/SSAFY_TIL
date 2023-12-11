import React from "react";
import { Canvas } from "@react-three/fiber";
import CustomGlobe from "./components/CustomGlobe";
import SingleCanvas from "./components/OrbitContrls";
import ThreeHTML from "./components/ThreeHTML";
import { View } from "react-native"
import Main from "./components/goMain";

export default function App() {

  return (
    <>
      <View>
        <Main/>
      </View>
      <CustomGlobe />
    </>
  )
}
