import {useState,useContext} from 'react'
import './main.css'
import { assets } from "../../assets/assets";
import ContextProvider from '../../Context/Context';
import { Context } from '../../Context/Context';
import { Loader}  from "lucide-react";

const Main = () => {

    const {onSent,recentPrompt,showResult,loading,resultData,setInput,input}=useContext(Context);
  return (
    <>
    <div className="main">
      <div className="nav">
        <p>Gemini</p>
        <img src={assets.user_icon} alt="" />

      </div>
      <div className="main-container">
        {!showResult ? 
        <>
        <div className="greet">
            <p><span>Hello, User</span></p>
            <p>Welcome back to Gemini AI Chatbot</p>

        </div>
        <div className="cards">
            <div className="card">
                <img src={assets.bulb_icon} alt="" />
                <p>Chat with Gemini</p>
            </div>
            <div className="card">
                <img src={assets.compass_icon} alt="" />
                <p>Chat with Gemini</p>
            </div>
            <div className="card">
                <img src={assets.code_icon} alt="" />
                <p>Chat with Gemini</p>
            </div>
        </div>
        </>
        :
        <div className="result">
            <div className="result-title">
                <img src={assets.user_icon} alt="" />
                <p>{recentPrompt}</p>
            </div>
            <div className="result-data">
                <img src={assets.gemini_icon} alt="" />
                {loading ?
            <div className="loading">
                <Loader className="animate-spin" />
            </div>:
                <p dangerouslySetInnerHTML={{__html:resultData}}/>}
            </div>
        </div>
        }
      </div>
      <div className="main-bottom">
          <div className="search-box">
              <input type="text" onChange={(e)=>{setInput(e.target.value)}} value={input} placeholder='Type your message here...' />
              <div className="div">
                  <img src={assets.gallery_icon} alt="" />
                  <img src={assets.mic_icon} alt="" />
                  <img onClick={()=>{onSent()}} src={assets.send_icon} alt="" />
              </div>
          </div>
          <p className="bottom-info">IT may be in acure me careful</p>
      </div>
    </div>
    </>
  )
}

export default Main
