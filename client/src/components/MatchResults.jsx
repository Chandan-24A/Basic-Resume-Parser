const MatchResults = ({ match }) => {
  const { score, matchedSkills, missingSkills, strengths, weaknesses, explanation, eligible } = match;

  // Ensure score is a number and handle potential undefined/null
  const numericScore = typeof score === 'number' ? score : 0;

  const getScoreColor = (score) => {
    if (score >= 80) return 'text-green-600';
    if (score >= 70) return 'text-yellow-600';
    return 'text-red-600';
  };

  const getStrokeColor = (score) => {
    if (score >= 80) return 'stroke-green-500';
    if (score >= 70) return 'stroke-yellow-500';
    return 'stroke-red-500';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 to-white">
      <div className="max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="bg-white rounded-2xl shadow-xl overflow-hidden border border-indigo-100">
          <div className="p-8">
            <h2 className="text-3xl font-extrabold text-center text-gray-900 mb-10">
              Resume Analysis Results
            </h2>

            {/* Score Card */}
            <div className="mb-10 flex flex-col items-center">
              <div className="relative w-40 h-40 flex items-center justify-center">
                <svg className="w-full h-full transform -rotate-90">
                  <circle
                    className="text-gray-200"
                    strokeWidth="10"
                    stroke="currentColor"
                    fill="transparent"
                    r="70"
                    cx="80"
                    cy="80"
                  />
                  <circle
                    className={`${getStrokeColor(numericScore)} transition-all duration-1000 ease-out`}
                    strokeWidth="10"
                    strokeDasharray={440}
                    strokeDashoffset={440 - (440 * numericScore) / 100}
                    strokeLinecap="round"
                    stroke="currentColor"
                    fill="transparent"
                    r="70"
                    cx="80"
                    cy="80"
                  />
                </svg>
                <div className="absolute text-3xl font-bold text-gray-900">
                  {numericScore}%
                </div>
              </div>
              <div className="mt-4 text-center">
                <h3 className="text-xl font-semibold text-gray-800">Match Score</h3>
                <p className={`mt-1 font-medium text-lg ${eligible ? 'text-green-600' : 'text-red-600'}`}>
                  {eligible ? '✓ Eligible for position' : '✕ Not eligible for position'}
                </p>
              </div>
            </div>

            {/* Grid Layout for Details */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {/* Matched Skills */}
              <div className="bg-green-50 rounded-xl p-6 border border-green-100">
                <h3 className="text-lg font-bold text-green-800 mb-4 flex items-center">
                  <span className="mr-2 text-2xl">✓</span> Matched Skills
                </h3>
                {matchedSkills?.length > 0 ? (
                  <div className="flex flex-wrap gap-2">
                    {matchedSkills.map((skill, index) => (
                      <span key={index} className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium">
                        {skill}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p className="text-green-700 italic">None identified</p>
                )}
              </div>

              {/* Missing Skills */}
              <div className="bg-red-50 rounded-xl p-6 border border-red-100">
                <h3 className="text-lg font-bold text-red-800 mb-4 flex items-center">
                  <span className="mr-2 text-2xl">⚠️</span> Skills to Develop
                </h3>
                {missingSkills?.length > 0 ? (
                  <div className="flex flex-wrap gap-2">
                    {missingSkills.map((skill, index) => (
                      <span key={index} className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm font-medium">
                        {skill}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p className="text-red-700 italic">None identified</p>
                )}
              </div>
            </div>

            {/* Strengths & Improvements */}
            <div className="grid grid-cols-1 gap-8 mt-8 md:grid-cols-2">
              {/* Strengths */}
              <div className="bg-blue-50 rounded-xl p-6 border border-blue-100">
                <h3 className="text-lg font-bold text-blue-800 mb-4 flex items-center">
                  <span className="mr-2 text-2xl">💪</span> Strengths
                </h3>
                {strengths?.length > 0 ? (
                  <ul className="space-y-2 list-disc list-inside text-blue-900">
                    {strengths.map((strength, index) => <li key={index}>{strength}</li>)}
                  </ul>
                ) : <p className="text-blue-700 italic">None identified</p>}
              </div>

              {/* Improvements */}
              <div className="bg-amber-50 rounded-xl p-6 border border-amber-100">
                <h3 className="text-lg font-bold text-amber-900 mb-4 flex items-center">
                  <span className="mr-2 text-2xl">📈</span> Areas for Growth
                </h3>
                {weaknesses?.length > 0 ? (
                  <ul className="space-y-2 list-disc list-inside text-amber-950">
                    {weaknesses.map((weakness, index) => <li key={index}>{weakness}</li>)}
                  </ul>
                ) : <p className="text-amber-800 italic">None identified</p>}
              </div>
            </div>

            {/* Explanation */}
            <div className="mt-8 p-6 bg-gray-50 rounded-xl border border-gray-100">
              <h3 className="text-lg font-bold text-gray-900 mb-3 flex items-center">
                <span className="mr-2 text-2xl">📝</span> Analysis Summary
              </h3>
              <p className="text-gray-700 leading-relaxed">{explanation}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MatchResults;