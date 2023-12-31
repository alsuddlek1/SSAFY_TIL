import * as React from 'react';
import { Canvas, useFrame } from '@react-three/fiber'


function Box(props) {
  const mesh = React.useRef(null)
  const [hovered, setHover] = React.useState(false)
  const [active, setActive] = React.useState(false)
  useFrame((state, delta) => (mesh.current.rotation.x += 0.01))
  return (
    <mesh
      {...props}
      ref={mesh}
      scale={active ? 1.5 : 1}
      onClick={(event) => setActive(!active)}
      onPointerOver={(event) => setHover(true)}
      onPointerOut={(event) => setHover(false)}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}


export default function Three() {
  return (
        <Canvas>
          <ambientLight />
          <pointLight position={[10, 10, 10]} />
          {/* <Box position={[0, -1, 0]} /> */}
          {/* <Box position={[0, 0, 0]} /> */}
          <Box position={[0, 1, 0]} />
          {/* <Box position={[0, 2, 0]} /> */}
        </Canvas>
  );
}