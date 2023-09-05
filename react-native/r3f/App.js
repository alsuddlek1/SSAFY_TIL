import * as React from 'react';
import { Canvas } from '@react-three/fiber';
import Three from './components/Three';
import CustomGlobe from './components/Globe';

export default function App() {
  return (
    <>
    <Canvas>
      <CustomGlobe/>
    </Canvas>
    </>
  );
}

