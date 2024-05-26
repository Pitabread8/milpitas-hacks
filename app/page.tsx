export default function Home() {
  return (
    <>
      <div className="font-serif">
        <div className="text-[#EEEEEE] h-screen w-screen flex justify-center items-center flex-col gap-2">
          <h1 className="text-[#EEEEEE] text-[150px] italic fade-up-right">The Truth Project</h1>
          <p className="py-2 w-2/3 text-center text-2xl leading-loose">Empower yourself with knowledge. Our website detects the political bias in the news you consume and offers concise summaries, helping you stay informed without bias.</p>
        </div>
        <div className="bg-white h-screen w-screen">
          <h1 className="text-6xl text-center pt-16">Summarizer</h1>
          <input type="text" placeholder="test" />
          <form action="/api/summarize" method="POST">
            <label htmlFor="url">Enter article URL:</label>
            <input type="text" id="url" name="url" required />
            <button type="submit">Summarize</button>
          </form>
        </div>
      </div>
    </>
  );
}
