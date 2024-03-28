import EasterEgg from '../assets/EasterEgg.png'

export default function Checkout () {
  return (
    <div className='checkoutScreenContainer'>
      <div className='loadingWheel'></div>
      <img src={EasterEgg} alt='easteregg photo'/>
    </div>
  )
}