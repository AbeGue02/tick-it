import { useNavigate } from "react-router-dom"

export default function Home() {
    // Might be repurposed to a login screen. For right now, it just takes the user to see venues
    let navigate = useNavigate()
    
    return (
        <div>
            <p>Home</p>
            <button 
                className="goldman-regular"
                onClick={() => navigate('/venues')}>Get started!</button>
        </div>
    )
}