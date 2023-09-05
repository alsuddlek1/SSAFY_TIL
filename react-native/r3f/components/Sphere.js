import * as React from 'react';
import { Canvas, useFrame } from '@react-three/fiber'

function Sphere(props){
    const mesh = React.useRef(null)
    
}

const SphereThree = () => {

    return(
        <Canvas
            camera={{
                fov: 75,
                position: [0, 0, 2.1]
            }}
            style={{
                cursor: 'move'
            }}
        >
            {/* <OrbitControls enableRotate={true} enableZoom={false} enablePan={false} /> */}
            <ambientLight intensity={1.3} />
            <pointLight position={[-10, -10, -10]} intensity={0.4} />
        </Canvas>
    )
}

export default SphereThree;