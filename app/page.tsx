export default function Home() {
  return (
    <>
      <div className="text-[#EEEEEE] font-serif">
        <div className="h-screen w-screen flex justify-center items-center flex-col gap-2">
          <h1 className="text-[150px] italic fade-up-right">Political Bias</h1>
          <p className="py-2">This is a paragraph about political bias.</p>
        </div>
        <div className="bg-yellow-300 h-screen w-screen">
          <h1 className="text-6xl text-center pt-16">Testing</h1>
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
