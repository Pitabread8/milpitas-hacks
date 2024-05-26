import Image from 'next/image'

export default function Home() {
  return (
    <>
      <div className="font-serif">
        <div className="text-[#EEEEEE] h-screen w-screen flex justify-center items-center flex-col gap-2">
          <h1 className="text-[#EEEEEE] text-[150px] italic fade-up-right">The Truth Project</h1>
          <p className="py-2 w-2/3 text-center text-2xl leading-loose">Empower yourself with knowledge. Our website detects the political bias in the news you consume and offers concise summaries, helping you stay informed without bias.</p>
        </div>
        <div className="bg-white h-screen w-screen flex flex-row items-start pt-16 justify-center">
          <div className="pl-12">
            <h1 className="text-6xl text-left">Get Your News, Quick.</h1>
            <form action="/api/summarize" method="POST">
              <p className="text-2xl leading-loose py-2 w-1/2">Paste a URL link, hit `enter`, and watch the magic happen. Our Summarizer will provide a concise and accurate summary of any political article so you can educate yourself in mere seconds.</p>
              <label htmlFor="url">Enter article URL:</label>
              <input type="text" id="url" name="url" required />
            </form>
          </div>
          <Image
            className="pr-12"
            src="/image.png"
            width={500}
            height={500}
            alt="Image"
          />
        </div>
      </div>
    </>
  );
}
