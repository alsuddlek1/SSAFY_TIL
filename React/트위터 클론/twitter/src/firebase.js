import { initializeApp } from 'firebase/app';
import { getAuth } from "firebase/auth";

const firebaseConfig = {
apiKey: 'your apiKey',
authDomain: 'nwitter-xxxx.firebaseapp.com',
projectId: 'nwitter-xxxx',
storageBucket: 'nwitter-xxx.appspot.com',
messagingSenderId: 'xxxxxxxxxx',
appId: 'xxxxxxx',
};

const app = initializeApp(firebaseConfig);

export const authService = getAuth();

export default app;